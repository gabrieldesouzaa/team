# Instructions for App Launch

To run this Streamlit application, you need to provide a Gemini API key.

1.  Create a file named `.env` in the root of this project.
2.  Add the following line to the `.env` file, replacing `"YOUR_API_KEY_HERE"` with your actual Gemini API key:

    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

3.  The `.env` file is listed in `.gitignore` and will not be committed to the repository.

Once the `.env` file is created, you can run the application with the following command:

```bash
streamlit run app.py
```
