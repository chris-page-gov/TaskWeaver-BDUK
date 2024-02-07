# Options for taskweaver_config.json

Notes
- that the code_generator and code_interpreter are implemented by TaskWeaver
- ${OPENAI_API_KEY} reads the environment variable which you will need to set
```json
{
    "llm.api_base": "https://api.openai.com/v1",
    "llm.api_key": "${OPENAI_API_KEY}",
    "llm.model": "gpt-4-1106-preview",
    "planner.use_experience": true,
    "code_generator.use_experience": true,
    "code_interpreter": {
        "code_verification_on": true,
        "allowed_modules": [
            "pandas",
            "matplotlib",
            "seaborn",
            "scipy",
            "sklearn",
            "torch",
            "nltk",
            "transformers",
            "PIL",
            "fastapi",
            "plotly"
        ],
        "blocked_functions": [
            "__import__",
            "eval",
            "exec",
            "execfile",
            "compile",
            "open",
            "input",
            "raw_input",
            "reload"
        ]
    }
}
```
## ollama

```json
{
    "llm.api_base": "https://localhost:11434",
    "llm.api_key": "ignored",
    "llm.type": "ollama",
    "llm.model": "mistral",
    "llm.response_format": null,
    "planner.use_experience": false,
    "code_generator.use_experience": false,
    "code_interpreter.code_verification_on": true,
    "code_interpreter": {
        "allowed_modules": ["numpy", "pandas", "matplotlib", "seaborn", "scipy", "sklearn", "tensorflow", "torch", "keras", "nltk", "spacy", "transformers", "gensim", "cv2", "PIL", "flask", "django", "fastapi", "streamlit", "pytorch_lightning", "keras", "xgboost", "lightgbm", "catboost", "statsmodels", "plotly", "dash", "bokeh", "altair", "shap", "lime", "eli5", "pdpbox", "shapash", "pycaret", "mlflow", "wandb", "optuna"],
        "allowed_classes": [
            "LinearRegression",
            "LogisticRegression",
            "DecisionTreeClassifier",
            "DecisionTreeRegressor",
            "RandomForestClassifier",
            "RandomForestRegressor",
            "GradientBoostingClassifier",
            "GradientBoostingRegressor",
            "XGBClassifier",
            "XGBRegressor",
            "LGBMClassifier",
            "LGBMRegressor",
            "CatBoostClassifier",
            "CatBoostRegressor",
            "SVC",
            "SVR"
        ],
        "blocked_functions": [
            "__import__", 
            "eval", 
            "exec", 
            "execfile", 
            "compile", 
            "open", 
            "input", 
            "raw_input", 
            "reload"
        ]
    },
"session.plugin_only_mode": false
}
```
All of the listed modules etc need to be avaiable in your python environment


> 💡 $\{AppBaseDir\} is the project directory.

> 💡 Up to 11/30/2023, the `json_object` and `text` options 
    of `llm.response_format` is only supported by the OpenAI models later than 1106. If you are using an older version of OpenAI model, you need to set the `llm.response_format` to `null`.

> 💡 Read [this](compression.md) for more information for 
    `planner.prompt_compression` and `code_generator.prompt_compression`.