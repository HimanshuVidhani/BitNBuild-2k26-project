import re

with open('c:/Users/vidha/OneDrive/Desktop/EcoScan-India-Enhanced/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

with open('c:/Users/vidha/OneDrive/Desktop/EcoScan-India-Enhanced/ecoscan-india-landing-v2 (1).html', 'r', encoding='utf-8') as f:
    landing_html = f.read()

# Extract landing page body content
landing_body_match = re.search(r'<body[^>]*>(.*?)</body>', landing_html, re.DOTALL)
landing_body = landing_body_match.group(1) if landing_body_match else ""

# Extract landing page styles and scripts from head
landing_styles_match = re.search(r'<style>(.*?)</style>', landing_html, re.DOTALL)
landing_styles = landing_styles_match.group(1) if landing_styles_match else ""

# Modify the handleLogin and handleSignup in landing_body to hide landing-page and show main-page
landing_body = landing_body.replace(
    "showAuthToast('Welcome back! You are now logged in.');",
    "showAuthToast('Welcome back! You are now logged in.');\n  setTimeout(() => { document.getElementById('landing-page').style.display = 'none'; document.getElementById('main-page').style.display = 'block'; }, 1000);"
)

landing_body = landing_body.replace(
    "showAuthToast('Account created successfully! Welcome to EcoScan India.');",
    "showAuthToast('Account created successfully! Welcome to EcoScan India.');\n  setTimeout(() => { document.getElementById('landing-page').style.display = 'none'; document.getElementById('main-page').style.display = 'block'; }, 1000);"
)

# Extract index main body content
index_body_match = re.search(r'(<body[^>]*>)(.*?)(</body>)', index_html, re.DOTALL)
index_body_start = index_body_match.group(1)
index_body_content = index_body_match.group(2)
index_body_end = index_body_match.group(3)

# Combine styles in index.html
if landing_styles:
    index_html = index_html.replace('</style>', f'{landing_styles}\n  </style>')

# Merge tailwind config manually or via regex
tailwind_config_addition = "glow:'0 0 30px -6px rgba(16,185,129,.45)'"
if "boxShadow: {" in index_html:
    index_html = index_html.replace("boxShadow: {", f"boxShadow: {{\n            'glow': '0 0 30px -6px rgba(16,185,129,.45)',")

# Combine the bodies
new_body_content = f"""
  <div id="landing-page">
{landing_body}
  </div>
  <div id="main-page" style="display: none;">
{index_body_content}
  </div>
"""

new_index_html = index_html[:index_body_match.start(2)] + new_body_content + index_html[index_body_match.end(2):]

with open('c:/Users/vidha/OneDrive/Desktop/EcoScan-India-Enhanced/index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)

print("Merged successfully")
