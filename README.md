# vercel-python

This is a simple Flask app ready to be deployed on Vercel.

## Setup

1. Install dependencies:
   ```bash
   /Users/tiphaine/Documents/histoireRI/.venv/bin/python -m pip install flask
   ```

2. Run locally:
   ```bash
   /Users/tiphaine/Documents/histoireRI/.venv/bin/python app.py
   ```

## Deploy to Vercel

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```
2. Create a `vercel.json` file (see below).
3. Run:
   ```bash
   vercel
   ```

## vercel.json

```
{
  "builds": [
    { "src": "app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "app.py" }
  ]
}
```
