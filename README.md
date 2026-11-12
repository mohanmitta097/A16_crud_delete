# Student CRUD — Complete

A browser-based student manager with all four CRUD operations.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000. API docs: http://127.0.0.1:8000/docs

## Operations
- Create: `POST /students`
- Read: `GET /students`
- Update: `PUT /students/{student_id}`
- Delete: `DELETE /students/{student_id}`

Data is in memory and resets when the server restarts.
