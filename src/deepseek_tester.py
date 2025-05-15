import requests
import json

API_KEY = "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"
MODEL = "google/gemini-2.0-flash-exp:free"


def process_content(content):
    return content.replace('<think>', '').replace('</think>', '')


def chat_stream(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    with requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            stream=True
    ) as response:
        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            return ""

        full_response = []

        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').replace('data: ', '')
                try:
                    chunk_json = json.loads(chunk_str)
                    if "choices" in chunk_json:
                        content = chunk_json["choices"][0]["delta"].get(
                            "content", "")
                        if content:
                            cleaned = process_content(content)
                            full_response.append(cleaned)
                except:
                    pass

        return ''.join(full_response)


def deepseek_tester_main(p):
    if p == 'math':
        user_input = 'Сгенерируй задачу по математике для 9 класса. Сначала выведи только целочисленный ответ(без каких-либо пояснений), затем ровно один пробел, а затем само условие задачи. Не добавляй никаких пояснений, не расписывай решение. Пример формата: "42 Найди значение выражения ..." — только одна строка.'
    elif p == 'inf':
        user_input = 'Сгенерируй задачу по информатике для 9 класса. Сначала выведи только целочисленный ответ(без каких-либо пояснений), затем ровно один пробел, а затем само условие задачи. Не добавляй никаких пояснений, не расписывай решение. Пример формата: "42 Найди значение выражения ..." — только одна строка'
    else:
        user_input = 'Сгенерируй задачу по физике для 9 класса. Сначала выведи только целочисленный ответ(без каких-либо пояснений), затем ровно один пробел, а затем само условие задачи. Не добавляй никаких пояснений, не расписывай решение. Пример формата: "42 Найди значение выражения ..." — только одна строка'

    a = chat_stream(user_input).strip()
    print('a:', a)

    if ' ' not in a:
        raise ValueError(f"Некорректный формат ответа от модели: '{a}'")

    ans, que = a.split(' ', 1)
    print('ans:', ans)
    print('que:', que)
    return ans, que


if __name__ == "__main__":
    deepseek_tester_main('math')
