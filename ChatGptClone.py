from openai import OpenAI
import time
def chat_with_gpt(prompt):

    client = OpenAI(
        api_key="" # --> create a openai key and past here
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    text = ""
    response = completion.choices[0].message.content.strip()
    for i in response.split(" "):
        yield i + " "
        time.sleep(0.06)


if __name__ == "__main__":
    import streamlit as sl
    sl.set_page_config(
        page_title="ChatGPT Clone",
        page_icon="img_2.png"
    )
    sl.markdown("<h1 style='text-align:center';>ChatGPT</h1>", unsafe_allow_html=True)
    question = sl.chat_input(placeholder="Enter Question")
    if question:
        sl.write_stream(chat_with_gpt(question))









