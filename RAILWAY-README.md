# 🚂 Railway Deployment Guide for BookVerse

## Quick Deploy Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

### 2. Create Railway Project
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your `Project-BookVerse` repository
5. Railway will auto-detect Python and start building

### 3. Add PostgreSQL Database
1. In your Railway project, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway will automatically set `DATABASE_URL` environment variable

### 4. Set Environment Variables
In Railway project settings → Variables, add:

```env
SECRET_KEY=<generate-random-secret-key>
ENV=production
DEBUG=False
MAX_UPLOAD_MB=50
IMPORT_MAX_MB=15
FREE_BOOK_LIMIT=5
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Deploy!
- Railway will automatically build and deploy
- Check logs for any issues
- Once deployed, visit your Railway URL

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'app'"
✅ **Fixed in start.sh** - PYTHONPATH is now set correctly

### Issue: Database connection errors
- Ensure PostgreSQL database is added to your Railway project
- Railway sets `DATABASE_URL` automatically
- Check it starts with `postgresql://` (not `postgres://`)

### Issue: Timeout errors
- Default timeout is 300s (5 minutes)
- Increase in `start.sh` if needed

### Issue: Storage/file upload issues
- Railway has ephemeral filesystem
- Files uploaded will be lost on restart
- For production, use S3/CloudFlare R2 (future enhancement)

## Monitoring

Check Railway logs:
```bash
# In Railway dashboard → Your service → Logs
```

Look for:
- ✓ "Created storage directories"
- ✓ "Database migrations completed"
- ✓ "Starting Gunicorn server"

## Scaling

Current configuration:
- 1 worker (good for Railway free tier)
- 300s timeout
- PostgreSQL with connection pooling

To scale up (Hobby plan):
- Increase workers in `start.sh` (e.g., `--workers 2`)
- Add Redis for caching
- Consider file storage service

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes (auto) | - | PostgreSQL connection (Railway sets this) |
| `SECRET_KEY` | Yes | - | Session encryption key |
| `ENV` | Yes | development | Set to `production` |
| `DEBUG` | No | True | Set to `False` in production |
| `PORT` | No (auto) | 8000 | Railway sets this automatically |
| `MAX_UPLOAD_MB` | No | 50 | Max file upload size |
| `FREE_BOOK_LIMIT` | No | 5 | Books allowed for free tier |

## Next Steps After Deploy

1. **Test the app** - Visit your Railway URL
2. **Create an account** - Sign up through the UI
3. **Upload a book** - Test file upload
4. **Import from Gutendex** - Test external API integration
5. **Monitor logs** - Watch for any errors

## Support

If deployment fails:
1. Check Railway logs for specific errors
2. Verify all environment variables are set
3. Ensure PostgreSQL database is connected
4. Check that `start.sh` has execute permissions (it should)

## Success Indicators

✅ Build completes without errors
✅ Health check at `/healthz` returns `{"ok": true}`
✅ App responds at Railway URL
✅ Can sign up and log in
✅ Can upload books
✅ Can import from Gutendex

**Your app should now be live! 🎉**

