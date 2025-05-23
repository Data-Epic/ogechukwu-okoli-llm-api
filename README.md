# University Applications Assistant

An assistant built with Python that provides information about university applications, powered by the [Groq](https://groq.com/) API and the `deepseek-r1-distill-llama-70b` LLM model. It handles university application questions based on applicants' queries.

---

## Features

- Responds to university applications customer inquiries and complaints in a detailed, clear, and helpful manner.
- Logs conversations and errors to a log file (`Educationalassistant.log`).
- Allows real-time interaction with the assistant via the command line.
- Uses environment variables (`.env` file) to protect sensitive credentials.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Data-Epic/ogechukwu-okoli-llm-api.git
   cd chatbo_t
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root and add your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

5. **Run the assistant from your terminal:**
   ```bash
   python chatbot.py
   ```

---

## Example Usage

- **You:** I need information on university applications in Nigeria
- **Assistant:** University applications in Nigeria typically involve several steps, primarily through the Joint Admissions and Matriculation Board (JAMB) for undergraduate programs. Here's a breakdown of the process...

---

## Limitations

- Responses are generated by a large language model and may not include exact admission requirements.
- Requires access to the internet and a valid Groq API key.
- Terminal-based interface only.

---

## Future Improvements

- Update data on universities and their admission requirements.
- Create a web app using Django or Flask.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute with attribution.

---

## Author

**Okoli Ogechukwu Abimbola**
- [Email](mailto:okoliogechi74@gmail.com)
- [GitHub](https://github.com/Human-Gechi)

