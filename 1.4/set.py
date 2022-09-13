st = { "Linux", "Macos", "Linux", "Win", "Win" }
print(st)
print("Linux" in st)

st.add("Solaris")
print(st)

st.discard("Win") # st.remove("Win")
st.discard("Win")
print(st)