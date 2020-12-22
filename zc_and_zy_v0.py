import pandas as pd
import streamlit as st
from datetime import datetime
from datetime import timedelta
from PIL import Image

LOVE_START_TIME = '2015-09-09'
FIRST_KISS_TIME = ''
FIRST_PLAY_TIME = ''


def  main():
    st.title("张灿和张玥的家")
    """
    ## 一. 开始
    """
    # %Y-%m-%d %H:%M:%S
    start_time = datetime.strptime(LOVE_START_TIME,'%Y-%m-%d')
    now_time = datetime.now()
    run_time = now_time - start_time
    days = run_time.days
    hours = run_time.seconds // (60*60)
    minutes = run_time.seconds % (60*60) // 60
    seconds = run_time.seconds % (60*60) % 60
    st.write(f'到今天已经相爱{days}天,{hours}小时,{minutes}分钟,{seconds}秒')
    

    """
    ## 二. 视频
    """
    for i in range(1,4):
        with open(f'pic/00{i}.mp4','rb') as video_file:
            video_bytes = video_file.read()
            st.video(video_bytes)

    """
    ## 三. 图片
    """
    for i in range(1,3):
        image = Image.open(f'pic/p00{i}.jpeg')
        st.image(image)


# >>> from PIL import Image
# >>> image = Image.open('sunrise.jpg')
# >>>
# >>> st.image(image, caption='Sunrise by the mountains',
# ...          use_column_width=True)



    return 

if __name__ == "__main__":
    main()



