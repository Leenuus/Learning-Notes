# nvim tips

## convert vimscript to lua

### global config

```vim
let g:bullets_enabled_file_types = [
    \ 'markdown',
    \ 'text',
    \ 'gitcommit',
    \ 'scratch'
    \]
```

```lua
vim.g.bullets_enabled_file_types = {'markdown', 'text', 'gitcommit', 'scratch'}
```
