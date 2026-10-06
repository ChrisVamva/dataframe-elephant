@echo off
rem One-time setup: inject your Tavily API key into goose's config (input hidden).
cd /d %~dp0
python set_tavily_key.py
pause
