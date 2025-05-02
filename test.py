import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

text = "This are a incorrect sentence."

matches = tool.check(text)

for match in matches:
    print(f"Error: {match.ruleId} - {match.message}")
    print(f"Suggested Corrections: {match.replacements}")
    print(f"Error Position: {match.offset}-{match.offset + match.errorLength}\n")
