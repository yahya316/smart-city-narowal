# The Smart City Narowal — Website

Static single-page website for **The Smart City Narowal**, a housing society in Narowal, Punjab, Pakistan.

## Stack

- Plain HTML / CSS / JavaScript
- No build step, no backend, no forms
- Ready for **GitHub Pages**

## Local preview

Open `index.html` in a browser, or serve the folder:

```bash
# Python
python -m http.server 8080

# Node
npx serve .
```

Then visit `http://localhost:8080`.

## Deploy on GitHub Pages

1. Create a GitHub repository and push this project.
2. Go to **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Select branch `main` (or `master`) and folder `/ (root)`.
5. Save — the site will be live at `https://<username>.github.io/<repo>/`.

If the site is served from a project subpath, keep asset paths relative (they already are).

## Project structure

```
├── index.html
├── css/styles.css
├── js/main.js
├── assets/images/
│   ├── logo.png          # Full logo (transparent, for dark backgrounds)
│   ├── logo-light.png    # Dark text variant for light backgrounds
│   ├── logo-icon.png     # Icon only
│   ├── logo-nav.png      # Compact navbar crop
│   └── hero-bg.jpg       # Hero background
└── scripts/              # Optional logo processing helpers
```

## Contact details used on the site

- **Address:** Near JMK Marquee, New Lahore Road, Narowal, 51600, Pakistan
- **Phone:** 0345-7772123
- **WhatsApp:** [wa.me/923457772123](https://wa.me/923457772123)
- **Facebook:** [facebook.com/602873452920346](https://www.facebook.com/602873452920346)

## Credits

Built by [Vixonics](https://vixonics.com).
