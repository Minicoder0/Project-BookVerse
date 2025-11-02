# 🚂 Deploy BookVerse to Railway

## ⚡ Quick Deploy (5 minutes)

### **Method 1: One-Click Deploy (Easiest)**

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template)

1. Click the button above
2. Connect your GitHub account
3. Select repository: `Project-BookVerse`
4. Railway will automatically:
   - Create a new project
   - Set up PostgreSQL database
   - Configure environment variables
   - Deploy your app

### **Method 2: Manual Deploy (More Control)**

#### **Step 1: Create Railway Account**
- Go to: https://railway.app
- Sign up with GitHub
- Free tier: $5 credit/month

#### **Step 2: Create New Project**
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **`Project-BookVerse`**
4. Railway detects Python and auto-configures

#### **Step 3: Add PostgreSQL Database**
1. Click **"New"** in your project
2. Select **"Database"**
3. Choose **"PostgreSQL"**
4. Railway automatically sets `DATABASE_URL`

#### **Step 4: Configure Environment Variables**
Railway auto-detects most variables, but add these:

```bash
SECRET_KEY = (click "Generate" or use command below)
ENV = production
SESSION_COOKIE_SECURE = True
MAX_UPLOAD_MB = 50
FREE_BOOK_LIMIT = 5
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

#### **Step 5: Deploy**
- Railway deploys automatically on push
- First deploy takes ~3-5 minutes
- Watch logs in the Railway dashboard

#### **Step 6: Access Your App**
- Railway provides a public URL: `https://your-app.railway.app`
- Click **"Generate Domain"** in Settings if not auto-generated

---

## 🔧 Configuration Files

Railway uses these files (already included):

- ✅ `Procfile` - Start command
- ✅ `requirements.txt` - Python dependencies
- ✅ `railway.json` - Railway-specific config
- ✅ `nixpacks.toml` - Build configuration
- ✅ `Dockerfile` - Container setup (optional)

---

## 📊 Post-Deployment

### **1. Run Database Migration**
Railway runs migrations automatically on startup via `Procfile`:
```
release: alembic upgrade head
web: gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

### **2. Create First User**
Visit your app URL and click **"Sign Up"**

### **3. Seed Public Books (Optional)**
Connect to Railway shell:
```bash
railway run python seed_public_books.py
```

Or use the import feature in the app:
- Login → Import → Quick seed 5 books

### **4. Monitor Your App**
Railway Dashboard shows:
- 📊 CPU & Memory usage
- 📝 Application logs
- 🔄 Deployment history
- 💾 Database metrics

---

## 🎯 Environment Variables Reference

### **Required:**
```bash
DATABASE_URL          # Auto-set by Railway PostgreSQL
SECRET_KEY           # Generate random string
ENV=production       # Sets production mode
```

### **Optional:**
```bash
SESSION_COOKIE_SECURE=True    # HTTPS only (recommended)
MAX_UPLOAD_MB=50              # File upload limit
FREE_BOOK_LIMIT=5             # Free tier book limit
PREMIUM_BOOK_LIMIT=999999     # Premium tier limit
PRO_BOOK_LIMIT=999999         # Pro tier limit
```

### **Advanced:**
```bash
REDIS_URL                     # If using Redis addon
STRIPE_SECRET_KEY             # For payments
STRIPE_WEBHOOK_SECRET         # Stripe webhooks
```

---

## 🔄 Updates & Redeployment

### **Automatic Deployment**
Railway auto-deploys when you push to GitHub:
```bash
git add .
git commit -m "Update feature"
git push origin main
```

### **Manual Redeploy**
In Railway dashboard:
1. Go to Deployments
2. Click **"Redeploy"** on any deployment

### **Rollback**
Click any previous deployment → **"Redeploy"**

---

## 🐛 Troubleshooting

### **App Won't Start**
Check Railway logs:
```
Settings → Logs → Filter by "error"
```

Common issues:
- Missing `SECRET_KEY` environment variable
- Database not connected
- Port binding issue (use `$PORT` variable)

### **Database Connection Error**
Verify `DATABASE_URL`:
```bash
railway variables
```

Should start with: `postgresql://...`

### **File Upload Issues**
Railway provides persistent storage by default.
Storage is in: `/app/storage/`

### **Performance Issues**
Upgrade Railway plan:
- Hobby: $5/month
- Pro: $20/month
- More CPU/RAM/storage

---

## 💰 Pricing

### **Free Tier** ($5 credit/month):
- ✅ 512 MB RAM
- ✅ Shared CPU
- ✅ 1 GB disk
- ✅ PostgreSQL database
- ⚠️ ~500 hours/month usage

### **Hobby** ($5/month):
- ✅ 8 GB RAM
- ✅ 8 vCPU
- ✅ 100 GB disk
- ✅ Faster deployments
- ✅ Priority support

---

## 🔗 Useful Links

- **Railway Dashboard**: https://railway.app/dashboard
- **Railway Docs**: https://docs.railway.app
- **Railway CLI**: https://docs.railway.app/develop/cli
- **Community Discord**: https://discord.gg/railway

---

## 🚀 Quick Commands (Railway CLI)

Install CLI:
```bash
npm install -g @railway/cli
```

Common commands:
```bash
railway login              # Login to Railway
railway link               # Link to project
railway logs               # View logs
railway run python manage.py  # Run commands
railway variables          # List env variables
railway up                 # Deploy current directory
railway status             # Check deployment status
```

---

## ✅ Deployment Checklist

- [ ] GitHub repository created
- [ ] Railway account created
- [ ] Project deployed from GitHub
- [ ] PostgreSQL database added
- [ ] `SECRET_KEY` environment variable set
- [ ] Domain generated
- [ ] App loads successfully
- [ ] User signup works
- [ ] Book upload works
- [ ] PDF reader works
- [ ] Books import from Gutendex

---

## 🎉 Success!

Your BookVerse app is now live on Railway!

**Next Steps:**
1. Share your app URL
2. Add custom domain (Settings → Domains)
3. Set up monitoring
4. Configure backups (PostgreSQL → Backups)

Need help? Open an issue on GitHub or ask in Railway Discord.

---

Made with ❤️ by BookVerse Team

