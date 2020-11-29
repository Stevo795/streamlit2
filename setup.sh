mkdir -p ~/.streamlit/



echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
prot = $PORT\n\
\n\
" > ~/.streamlit/config.toml