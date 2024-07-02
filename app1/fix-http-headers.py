from bs4 import BeautifulSoup
import os

def fix_headers(report_file, index_js_file):
    with open(report_file, "r") as f:
        report = BeautifulSoup(f, "html.parser")

    hsts_found = False
    xframe_found = False
    secure_cookie_found = False
    httponly_cookie_found = False
    cacheable_response_found = False

    for issue in report.find_all("h2"):
        if "Strict transport security not enforced" in issue.text:
            hsts_found = True
        if "Frameable response (potential Clickjacking)" in issue.text:
            xframe_found = True
        if "TLS cookie without secure flag set" in issue.text:
            secure_cookie_found = True
        if "Cookie without HttpOnly flag set" in issue.text:
            httponly_cookie_found = True
        if "Cacheable HTTPS response" in issue.text:
            cacheable_response_found = True

    with open(index_js_file, "r") as f:
        index_js = f.read()

    # Adicionar headers conforme necessário
    if hsts_found:
        index_js = index_js.replace(
            "res.write('Hello World! ' + os.hostname());",
            "res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');\n  res.write('Hello World! ' + os.hostname());"
        )
    if xframe_found:
        index_js = index_js.replace(
            "res.write('Hello World! ' + os.hostname());",
            "res.setHeader('X-Frame-Options', 'DENY');\n  res.write('Hello World! ' + os.hostname());"
        )
    if secure_cookie_found:
        # Assumindo que você está definindo cookies em outro lugar no código
        index_js = index_js.replace(
            "res.cookie('nome_do_cookie', valor_do_cookie);",
            "res.cookie('nome_do_cookie', valor_do_cookie, { secure: true });"
        )
    if httponly_cookie_found:
        index_js = index_js.replace(
            "res.cookie('nome_do_cookie', valor_do_cookie);",
            "res.cookie('nome_do_cookie', valor_do_cookie, { httpOnly: true });"
        )
    if cacheable_response_found:
        index_js = index_js.replace(
            "res.write('Hello World! ' + os.hostname());",
            "res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, private');\n  res.setHeader('Pragma', 'no-cache');\n  res.write('Hello World! ' + os.hostname());"
        )

    with open(index_js_file, "w") as f:
        f.write(index_js)


# Chame a função com os caminhos para o relatório do Burp e o arquivo index.js
fix_headers("scan-results/burp-report.html", "app1/index.js")