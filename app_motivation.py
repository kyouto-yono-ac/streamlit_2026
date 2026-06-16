import streamlit as st

st.title("🚀 授業のやる気診断アプリ")
st.write("今のあなたの状態を入力して、やる気を計測してみましょう！")

st.markdown("---")

# 1. 眠さ加減を入力 (0: 冴えている, 100: 眠りそう)
sleepiness = st.slider("1. 今の眠さ加減はどれくらいですか？", 0, 100, 20, help="0に近いほど目が冴えています")

# 2. 授業の理解度を入力 (0: 全くわからない, 100: 完璧)
understanding = st.slider("2. 今の授業の内容をどれくらい理解していますか？", 0, 100, 50, help="100に近いほど理解できています")

# 3. 他のことを考えている回数を入力
distractions = st.number_input("3. 授業中に他のこと（スマホや雑念など）を考えてしまった回数は？", min_value=0, value=0, step=1)

st.markdown("---")

# やる気の計算ロジック (シンプルな重み付け)
# ベースを理解度とし、眠気と雑念を減点方式で計算します
base_motivation = (understanding * 0.6) + ((100 - sleepiness) * 0.4)
penalty = distractions * 5
final_motivation = base_motivation - penalty

# 0%〜100%の範囲に収める
final_motivation = max(0, min(100, int(final_motivation)))

# 結果の表示
if st.button("やる気を計測する", use_container_width=True):
    st.write(f"### あなたの今のやる気は... **{final_motivation}%** です！")
    
    if final_motivation >= 80:
        st.success("素晴らしい！今の調子で授業を楽しみましょう！🌟")
        st.balloons()
    elif final_motivation >= 50:
        st.info("まずまずのやる気です。少し背筋を伸ばしてリフレッシュしましょう。😊")
    elif final_motivation >= 20:
        st.warning("少し集中が切れているかもしれません。顔を洗ったり深呼吸してみましょう。🍵")
    else:
        st.error("やる気がかなり低下しています。無理せず、まずは目を開けることから始めましょう。😴")

st.caption("※この数値は入力された項目に基づく簡易的な目安です。")