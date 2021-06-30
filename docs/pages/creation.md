---
layout: default
title: about
image: /assets/images/hackers-1.jpg
---


# Notes on how I set up this site...


- [jekyll official docs](https://jekyllrb.com/docs/)
- [jekyll w/ bootstrap guide](https://medium.com/better-programming/an-introduction-to-using-jekyll-with-bootstrap-4-6f2433afeda9)
- [bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)


1. install or update ruby (apt or brew)
2. install jekyll and bundler: `gem install bundle jekyll`
3. clone a fresh repo: `clone https://github.com/myrepo`
5. init a new jekyll site: `jekyll new docs --blank`
4. move into site dir: `cd docs/`
5. Create Gemfile: `bundle init`
6. Add jekyll to Gemfile: `echo "gem 'jekyll'" >> ./Gemfile`
7. Install gems and create Gemfile.lock: `bundle`
8. Serve site: `bundle exec jekyll serve -w`
9. edit site with text editor: `subl .`
10. Edit the config.yml...


