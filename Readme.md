# Next-Life App

🏠 **Next-Life** is a personal life management application built with Python and Kivy. It helps users balance various aspects of their life such as health, family, work, leisure, finance, personal growth, community, spirituality, and insights.

## Features

- **Health Management**: Track your daily steps, calories, and sleep patterns.
- **Family and Relationships**: Manage your time with family and relationships.
- **Work and Career**: Set professional goals and track progress.
- **Leisure & Hobbies**: Organize and manage your hobbies and leisure time.
- **Financial Management**: Monitor your expenses and savings.
- **Personal Growth**: Track self-improvement goals.
- **Community Engagement**: Get involved with your community and contribute to social causes.
- **Spirituality & Meaning**: Keep track of your spiritual journey.
- **Insights**: Receive personalized insights and recommendations based on your habits.

## Screenshots

Here are some screenshots from the app:

![Home Screen](assets/screenshots/home_screen.png)
![Health Screen](assets/screenshots/health_screen.png)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/next-life-app.git
    cd next-life-app
    ```

2. **Install the dependencies**:
    Make sure you have Python 3.x installed on your machine. Then install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the App

To run the app, simply execute the following command:

```bash
python main.py
```

This will launch the app window where you can explore the various screens and features.

## Project Structure

```
Next-Life/
├── assets/                 # Assets like fonts and images
│   ├── fonts/              # Font files (e.g., NotoColorEmoji.ttf)
│   └── screenshots/        # Screenshot images for README
├── screens/                # All screen files (e.g., health_screen.py, home_screen.py)
├── main.py                 # The main entry point for the app
├── app.py                  # Core app logic
├── requirements.txt        # List of dependencies for the project
└── README.md               # Project README file
```

## Dependencies

- [Kivy](https://kivy.org/) - Python framework for developing multitouch applications.
- `Noto Color Emoji` font for emoji support in the app.

To install all required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

Once the app is running, you can navigate through the various life management categories by clicking the corresponding buttons in the top navigation bar. Each screen provides a summary and allows for tracking or setting goals in the given category.

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push the changes to your branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to open issues or submit pull requests to improve the app!
