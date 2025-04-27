from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import json
import uvicorn

app = FastAPI()


@app.get("/")
def hey():
     return {
         "message": "Hiiii, How are you)"
    }

@app.get("/items/")
def get_items():
    results = []
    for i in range(17):
        result = {"title": None,
                      "link": None}
        
        r = requests.get(f"https://милкагросервис.рф/category/{i}")
        content = r.text
        soup = BeautifulSoup(content, "html.parser")
        divs = soup.find_all("div", class_="product__details")
        for div in divs:
            link_tag = div.find('a')
            if link_tag:
                title = ' '.join(link_tag.text.strip().split())
                link = f"https://милкагросервис.рф{link_tag.get('href', '')}"
                result["title"] = title
                result["link"] = link
                results.append(result)

    return results

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

