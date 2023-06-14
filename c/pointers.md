# A Note on MyCodeSchool C Pointer Course

## 动态分配和释放内存

```
malloc(size) // without init
calloc(num, size_of_one) // init these mem to 0
realloc(pointer_to_realloc, new_size) 
realloc(pointer_to_realloc, 0) // eq to free(pointer_to_realloc)
realloc(NULL, size) // eq to malloc
```


