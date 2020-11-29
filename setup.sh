mkdir -p ~/.streamlit/

echo"\
[general]\n\
email = \"gitduck@protonmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo"\
[server]\n\
headless = true\n\
enableCORS = false\n\
prot = $PORT\n\
"> ~/.streamlit/config.toml