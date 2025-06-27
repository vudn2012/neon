import streamlit as st

st.set_page_config(page_title='Bạn thân của tôi', page_icon=':sparkling_heart:', layout='wide')
st.title('📒 Danh sách những người bạn thân')

col1, col2, col3 = st.columns(3)

Friends = {
    'Minh': {'Tuổi': 20, 'Sở thích': 'Đá bóng, đọc sách', 'Ghi chú': 'Vui vẻ, hay giúp đỡ'},
    'Hoa': {'Tuổi': 21, 'Sở thích': 'Vẽ, nghe nhạc', 'Ghi chú': 'Quan tâm người khác'},
    'Long': {'Tuổi': 19, 'Sở thích': 'Game, đi phượt', 'Ghi chú': 'Trung thành, vui tính'}
}

with col1:
    b1 = st.button('Minh')
with col2:
    b2 = st.button('Hoa')
with col3:
    b3 = st.button('Long')

if b1:
    with st.expander('Thông tin về Minh'):
        st.write(Friends['Minh'])
if b2:
    with st.expander('Thông tin về Hoa'):
        st.write(Friends['Hoa'])
if b3:
    with st.expander('Thông tin về Long'):
        st.write(Friends['Long'])

with st.sidebar:
    st.subheader('🧡 Người bạn được chọn:')
    if b1:
        st.write('Minh – người bạn thân từ thuở nào!')
    elif b2:
        st.write('Hoa – cô bạn nhẹ nhàng, đáng yêu.')
    elif b3:
        st.write('Long – chiến hữu không thể thiếu.')
