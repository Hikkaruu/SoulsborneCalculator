@echo off
start "Backend" cmd /k "cd backend && fastapi dev"
start "Frontend" cmd /k "cd frontend && ng serve"
timeout 3
start http://localhost:8000
start http://localhost:4200
pause