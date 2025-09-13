import pymupdf  # 导入PyMuPDF

file_path = "build_arm_part1.pdf"

def analyze_text_format(pdf_path):
    """
    分析PDF指定页面中文本的格式，包括字体、字号和是否粗体。
    
    参数:
        pdf_path: PDF文件路径
        page_num: 要分析的页面编号（从0开始）
    """
    text_list = []
    doc = pymupdf.open(pdf_path)
    for i,page in enumerate(doc):
        # 获取页面文本的完整字典结构
        page_dict = page.get_text("dict")
        # 遍历blocks -> lines -> spans
        for block in page_dict["blocks"]:
            block_text = []
            score = 0
            if block["bbox"][1]<740 and block["bbox"][3]>50:
                if "lines" in block:  # 确保是文本块
                    if len(block["lines"])==1:
                        score += 3
                    if block["lines"][0]["spans"][0]["font"] == "Arial-BoldMT":
                        score += 1
                    if block["lines"][0]["spans"][0]["flags"] == 16:
                        score += 1
                    if int(block["lines"][0]["spans"][0]["size"]) >= 14:
                        score += 1
                    for line in block["lines"]:
                        for span in line["spans"]:
                            # 提取关键信息
                            text = span["text"]
                            font = span["font"]  # 字体名称
                            size = span["size"]  # 字号（浮点数，单位是pt）
                            flags = span["flags"]  # 样式标志位（二进制位存储）
                            block_text.append(text)
                
                    block_dict = {"page_num":i ,"score":score, "block_text":" ".join(block_text)}
                    text_list.append(block_dict)
    doc.close()
    return text_list

list_result = analyze_text_format(file_path)


chunk_list = []
tmp = []
chunk_size = 3000
for i, para in enumerate(list_result):
    if len(para["block_text"]) > chunk_size:
        chunks = [para["block_text"][i:i+chunk_size] for i in range(0, len(para["block_text"]), chunk_size)]
        chunk_list.extend(chunks)
    elif len(" ".join(tmp) + para["block_text"]) > chunk_size:
        tmp_title = tmp[0]
        chunk_list.append(tmp)
        tmp = [tmp_title]
    if para["score"]>4:
        if len(tmp)>0:
            chunk_list.append(tmp)
        tmp = [para["block_text"]]
    elif list_result[i-1]["block_text"][-1] not in ".:;" and list_result[i]["block_text"][0].islower():
        tmp[-1] += " "+para["block_text"]
    else:
        tmp.append(para["block_text"])

with open("output_chunk.txt", 'w', encoding='utf-8') as f:
    for chunk in chunk_list:
        chunk_text = "\n".join(chunk)
        if len(chunk_text)>3000:
            print(chunk[0], len(chunk_text))
        f.write(chunk_text + '\n\n')
