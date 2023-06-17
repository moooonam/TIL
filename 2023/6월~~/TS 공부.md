## 유튜브 강의 들으며 TS 공부

```ts
interface Info {
    name: string,
    age: number
}

const myInfo = {
    name: "무남",
    age :28
}

const sayHello = (person: Info): string => {
    return `안녕 ${person.name} 나이는 ${person.age}`
}
```