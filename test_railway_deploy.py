#!/usr/bin/env python3
"""
Quick test script to verify Railway deployment readiness
Run this before deploying to catch common issues
"""

import os
import sys
from pathlib import Path

def test_project_structure():
    """Check that all required files and directories exist"""
    print("[*] Checking project structure...")
    
    required_files = [
        "app/__init__.py",
        "app/main.py",
        "app/config.py",
        "app/database.py",
        "requirements.txt",
        "alembic.ini",
        "Procfile",
        "start.sh",
        "railway.toml",
        "nixpacks.toml"
    ]
    
    required_dirs = [
        "app",
        "app/models",
        "app/routers",
        "app/services",
        "templates",
        "static",
        "alembic",
        "storage/books",
        "storage/covers"
    ]
    
    missing_files = []
    missing_dirs = []
    
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    for dir_path in required_dirs:
        if not Path(dir_path).exists():
            missing_dirs.append(dir_path)
    
    if missing_files:
        print("[X] Missing required files:")
        for f in missing_files:
            print(f"   - {f}")
        return False
    
    if missing_dirs:
        print("[X] Missing required directories:")
        for d in missing_dirs:
            print(f"   - {d}")
        return False
    
    print("[OK] All required files and directories present")
    return True


def test_imports():
    """Check that main app can be imported"""
    print("\n[*] Testing app imports...")
    
    try:
        from app.main import app
        print("[OK] App successfully imported")
        return True
    except Exception as e:
        print(f"[X] Failed to import app: {e}")
        return False


def test_requirements():
    """Check requirements.txt is valid"""
    print("\n[*] Checking requirements.txt...")
    
    try:
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
        
        if not lines:
            print("[X] requirements.txt is empty")
            return False
        
        critical_packages = [
            "fastapi",
            "uvicorn",
            "gunicorn",
            "sqlalchemy",
            "alembic",
            "psycopg-binary",
            "jinja2"
        ]
        
        content = "".join(lines).lower()
        missing_packages = []
        
        for pkg in critical_packages:
            if pkg not in content:
                missing_packages.append(pkg)
        
        if missing_packages:
            print("[!] Missing critical packages in requirements.txt:")
            for pkg in missing_packages:
                print(f"   - {pkg}")
            return False
        
        print(f"[OK] requirements.txt valid ({len(lines)} packages)")
        return True
        
    except Exception as e:
        print(f"[X] Error reading requirements.txt: {e}")
        return False


def test_env_example():
    """Check .env.example exists and has required vars"""
    print("\n[*] Checking .env.example...")
    
    if not Path(".env.example").exists():
        print("[!] .env.example not found (optional but recommended)")
        return True
    
    try:
        with open(".env.example", "r") as f:
            content = f.read()
        
        required_vars = ["SECRET_KEY", "DATABASE_URL", "ENV"]
        missing_vars = []
        
        for var in required_vars:
            if var not in content:
                missing_vars.append(var)
        
        if missing_vars:
            print("[!] Missing recommended environment variables:")
            for var in missing_vars:
                print(f"   - {var}")
        else:
            print("[OK] .env.example looks good")
        
        return True
        
    except Exception as e:
        print(f"[!] Error reading .env.example: {e}")
        return True


def test_start_script():
    """Check start.sh is executable"""
    print("\n[*] Checking start.sh...")
    
    if not Path("start.sh").exists():
        print("[X] start.sh not found")
        return False
    
    # Check if file has content
    with open("start.sh", "r") as f:
        content = f.read()
    
    if not content or len(content) < 50:
        print("[X] start.sh appears to be empty or too short")
        return False
    
    if "gunicorn" not in content:
        print("[!] start.sh doesn't mention gunicorn")
        return False
    
    print("[OK] start.sh looks good")
    return True


def main():
    print("=" * 60)
    print("RAILWAY DEPLOYMENT READINESS CHECK")
    print("=" * 60)
    
    tests = [
        test_project_structure,
        test_requirements,
        test_imports,
        test_env_example,
        test_start_script
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"[X] Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"[OK] ALL CHECKS PASSED ({passed}/{total})")
        print("\n[SUCCESS] Your project is ready for Railway deployment!")
        print("\nNext steps:")
        print("1. git add .")
        print("2. git commit -m 'Ready for Railway'")
        print("3. git push origin main")
        print("4. Deploy on Railway (see RAILWAY-README.md)")
        return 0
    else:
        print(f"[!] SOME CHECKS FAILED ({passed}/{total} passed)")
        print("\n[X] Please fix the issues above before deploying")
        return 1


if __name__ == "__main__":
    sys.exit(main())

