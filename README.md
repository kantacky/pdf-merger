# PDF Merger

片面スキャンした書籍の PDF2 つを 1 つの PDF ファイルの統合します。

## Prerequirement

- macOS
- brew
  <details>
  <summary>インストール方法</summary>

  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile
  eval $(/opt/homebrew/bin/brew shellenv)
  ```

  </details>

- pyenv
  <details>
  <summary>インストール方法</summary>

  ```
  brew update
  brew install pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
  ```

  </details>

- cmake
  <details>
  <summary>インストール方法</summary>

  ```
  brew update
  brew install cmake
  ```

  </details>

## Setup

```
make install
```

## How to Use

```
make merge ODD=~/Downloads/odd.pdf EVEN=~/Downloads/even.pdf OUT=~/Downloads/merged.pdf
```

&copy; 2025 Kanta Oikawa
