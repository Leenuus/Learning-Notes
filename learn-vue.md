# Vue Learning Notes

## Boilerplate and data model
```js
{
    // use {{field}} to access data
    template:"",
    data(){
        // return a object defining the data
        return {
            field: ""
        }
    },
    // use this.field to access data defined in data()
    methods:{
        func1(){

        },
        func2(){

        },
    },
    props: [],
    // hooks
    created(){

    },
    mounted(){

    }
}
```

```html
<script>
    const app = 
</script>
```

## Concepts

### lifecycle and hooks

Hooks are just some functions which is executed when something happen(callback).

#### stages of lifecycle

1. beforeCreate
2. created
3. beforemount
4. mounted
5. beforeupdate
6. updated
7. beforeDestory
8. Destoryed

### directive

1. name
2. argument
3. modifier
4. value

```vue
v-on:submit.prevent="onSubmit"
```

#### name

1. v-on, shorthand: `@`
2. v-bind, shorthand: `:`
3. v-if, v-else
