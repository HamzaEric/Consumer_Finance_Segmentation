# index.py
from app import app
from src.layouts import build_layout
import src.callbacks  # Crucial: forces callback registration with the app instance


server = app.server
# ------------------------

app.layout = build_layout()

if __name__ == "__main__":
    # Standard terminal deployment run execution
    app.run(debug=True, host="0.0.0.0", port=9000)