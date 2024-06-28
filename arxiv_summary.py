import openai
import pandas as pd
import time
# import requests
# from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import feedparser

#设置OpenAI API密钥
openai.api_key = "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"

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model ="gpt-4",
        messages=[
        {"role": "system", "content":"You are a helpful assistant."},
        {"role":"user","content":prompt}
        ]
    )
    print(response)
    summary = response["choices"][0]["message"]["content"].strip()
    return summary


def get_arxiv_html(input_num = 400):
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = 'cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.CV+OR+cat:cs.LG'  # 只搜索cs.CL、cs.HC和cs.CV类别
    start = 0
    max_results = 400  # 获取的论文数量
    if input_num != 0:
        max_results = input_num

    sort_by = 'submittedDate'  # 按提交日期排序
    sort_order = 'descending'  # 降序排列
    # 构建API请求URL
    query_url = f"{base_url}search_query={search_query}&start={start}&max_results={max_results}&sortBy={sort_by}&sortOrder={sort_order}"

    # 使用urllib.request获取API响应
    with urllib.request.urlopen(query_url) as response:
        xml_data = response.read()

    # 使用feedparser解析API响应
    parsed_data = feedparser.parse(xml_data)
    return parsed_data

def get_number_from_user():
    input_num = input("Enter paper amount(Max 2000, default 300): ")
    if input_num == "":
        input_num = 0
    else:
        input_num = abs(int(input_num))
    if input_num > 2000:
        input_num = 2000
    return input_num

def get_and_write_excel():
    # 创建一个空的DataFrame，用于存储论文信息
    columns = ['Title', 'Published','Summary']
    papers_df = pd.DataFrame(columns=columns)

    llm_keywords = ["llm","gpt","language model","foundation model","chain of thought","sota",
        "palm","chatbot","llama","Gemini", "RAG", "mixtral",
        "pre-train","generative","transformer","prompt","token","inference","expert","parameters","vision","mixture",
        "agent","multi-modal","multimodal","ai","reinforced","reinforcement","rlhf"]
    vision_related_keywords = ["diffusion","midjourney","vision","visual","image","shape","augmentation","segmentation"]
    game_related_keywords = ["game","agent","aigc","AI","simulate","2D","3D","audio","video","bot","NPC","scene"]
    unrelated = ["protein","medical","medicine","chemical","chemistry","biological"]

    #check if only 10 get and try again
    input_num = get_number_from_user()
    parsed_data = get_arxiv_html(input_num)
    entry_length = len(parsed_data.entries)
    print("entry_length",entry_length)
    print("first entry \n",parsed_data.entries[0])
    if entry_length < int(input_num):
        parsed_data = get_arxiv_html(input_num)
        print(entry_length)
        print(f"Get only {entry_length}. Retry to get complete version")

    # 将论文信息添加到DataFrame中
    for entry in parsed_data.entries:
    #initialze settings
        title = entry.title
        published = entry.published
        abs_link = entry.link
        summary = entry.summary
        category = entry.arxiv_primary_category['term']
        pdf_link = None

    #initialze scores
        is_llm_related_score = 0
        is_vision_related_score = 0
        is_game_related_score = 0

        for link in entry['links']:
            if link.get('title')  == 'pdf':
                pdf_link = link['href']
                break

        for keyword in llm_keywords:# Check llm related score
            if keyword.lower() in title.lower():
                is_llm_related_score += 3
            if keyword.lower() in summary.lower():
                is_llm_related_score += 1

        for keyword in vision_related_keywords: # Check vision related score
            if keyword.lower() in title.lower():
                is_vision_related_score += 3
                is_llm_related_score -= 1
            if keyword.lower() in summary.lower():
                is_vision_related_score += 1
                is_llm_related_score -= 1

        for keyword in game_related_keywords: # Check game related score
            if keyword.lower() in title.lower():
                is_game_related_score += 1
            if keyword.lower() in summary.lower():
                is_game_related_score += 1

        for keyword in unrelated: # Check game related score
            if keyword.lower() in title.lower():
                is_llm_related_score -= 3
            if keyword.lower() in summary.lower():
                is_llm_related_score -= 1

        if "game" in title.lower():
            is_game_related_score += 3
        if "game" in summary.lower():
            is_game_related_score += 2

        # 将论文信息添加到DataFrame中
        newrow = {'Title': title, 'Summary': summary,'Category': category,'Published': published,
            'Link': abs_link, 'pdf_link': pdf_link,
            "is_llm_related":is_llm_related_score,"is_vision_related_score":is_vision_related_score,"is_game_related_score":is_game_related_score}
        papers_df = pd.concat([papers_df,pd.DataFrame.from_records([newrow])], ignore_index=True)

    # 将DataFrame保存到Excel文件中
    import os

    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_file = os.path.join(desktop_path, "arxiv_papers.xlsx")
    print(desktop_path)
    print(output_file)
    try:
        papers_df.to_excel(output_file, index=False, engine='openpyxl')
    except:
        papers_df.to_excel(f'arxiv_papers_{published[:13]}.xlsx', index=False, engine='openpyxl')

    input("Press Enter to exit...")

get_and_write_excel()
