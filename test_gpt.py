import openai

# ✅ Replace with your actual OpenAI API Key
openai.api_key = "sk-proj-CA8Yh4pADCMrnwJnloE_JxKl2So"
def test_gpt4():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a highly knowledgeable mortgage AI assistant helping real estate investors."},
                {"role": "user", "content": "Tell me about DSCR loans."}
            ],
            max_tokens=500,
            temperature=0.7
        )
        print(response["choices"][0]["message"]["content"])
    except Exception as e:
        print(f"Error connecting to GPT-4: {e}")

# Run the test
if __name__ == "__main__":
    test_gpt4()
