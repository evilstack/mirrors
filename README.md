![Arch Linux last sync](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/evilstack/b24a1fa2b005e5fce6fb11e1c6712559/raw/arch-status.json)
![Termux last sync](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/evilstack/b24a1fa2b005e5fce6fb11e1c6712559/raw/termux-status.json)

# Mirrors

Public mirrors for fun and (*no*) profit.  
This is a solo hobby project. Performance and reliability are prioritized, nothing is guaranteed.

<br>

## Arch Linux

Synced from `mirrors.rit.edu/archlinux` hourly; */other*, */sources*, and */archive* excluded.

This mirror can be used by including it in `/etc/pacman.d/mirrorlist`  
```
Server = http://pkg.evlstk.dev/archlinux/$repo/os/$arch
```

or  


```
Server = https://pkg.evlstk.dev/archlinux/$repo/os/$arch
```

<br>

## Termux
Synced from `packages.termux.dev/termux` bi-hourly; *termux-main-21* excluded.

This mirror can be used by including it in `$PREFIX/etc/apt/sources.list`  
```
deb http://pkg.evlstk.dev/termux/termux-main stable main
deb http://pkg.evlstk.dev/termux/termux-root root stable
deb http://pkg.evlstk.dev/termux/termux-x11 x11 main
```

or  

```
deb https://pkg.evlstk.dev/termux/termux-main stable main
deb https://pkg.evlstk.dev/termux/termux-root root stable
deb https://pkg.evlstk.dev/termux/termux-x11 x11 main
```

<br>

## Issues
Problems may be reported by opening an issue here.

<br>

## Security Issues
Please report security issues privately:

1. Use **Security → Report a vulnerability** on this repository (GitHub private vulnerability
   reporting).
2. If that option isn't available, open an issue that says you have a security report and omit
   the details; I'll arrange a private channel.
