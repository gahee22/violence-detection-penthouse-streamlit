import numpy as np
import pandas as pd 
import streamlit as st

def main():
    st.title("Violence Detection in drama 'Penthouse'")
    add_selectbox = st.sidebar.selectbox("Select document", ("Summary", "시즌1 1화 video", "시즌1 1화 excel", "시즌1 17화 video", "시즌1 17화 excel", "시즌1 19화 video", "시즌1 19화 excel"))
    if add_selectbox == "Summary":
        st.subheader("Summary")
        st.write("----")
        st.write("\n")
        st.write("✅ Code : [Real-life-violence-detection](https://github.com/NANDINI-star/Real-life-violence-detection)")
        st.write("✅ Network : MobileNetV2 (created on kaggle)")
        st.write("✅ Dataset : [Real Life Violence Situations Dataset](https://www.kaggle.com/datasets/mohamedmustafa/real-life-violence-situations-dataset)")
        st.write("✅ Training & Validation Result : Accuracy on train 0.915 , Loss on train 0.214 , Accuracy on validation 0.902, Loss on validation 0.244")
    elif add_selectbox == "시즌1 1화 video":
        st.subheader("시즌1 1화 video")
        st.write("----")
        st.write("\n")
        video_file = open('data/video/output1-1.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif add_selectbox == "시즌1 1화 excel":
        st.subheader("시즌1 1화 excel")
        st.write("----")
        st.write("\n")
        df = pd.read_csv('data/excel/result_final_output1-1.csv')
        st.dataframe(df)

    elif add_selectbox == "시즌1 17화 video":
        st.subheader("시즌1 17화 video")
        st.write("----")
        st.write("\n")
        video_file = open('data/video/output1-17.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif add_selectbox == "시즌1 17화 excel":
        st.subheader("시즌1 17화 excel")
        st.write("----")
        st.write("\n")
        df = pd.read_csv('data/excel/result_final_output1-17.csv')
        st.dataframe(df)

    elif add_selectbox == "시즌1 19화 video":
        st.subheader("시즌1 19화 video")
        st.write("----")
        st.write("\n")
        video_file = open('data/video/output1-19.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    elif add_selectbox == "시즌1 19화 excel":
        st.subheader("시즌1 19화 excel")
        st.write("----")
        st.write("\n")
        df = pd.read_csv('data/excel/result_final_output1-19.csv')
        st.dataframe(df)

    
if __name__ == '__main__':
    main()

