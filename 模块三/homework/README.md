用户表
```json
{
  "root" : {
    "id" : "0001",
    "username" : "root",
    "password" : "root",
    "role" : "Teacher|Student|root"
  }
}
```

Student表
```json
{
  "Alvin" : {
    "id" : "0002",
    "username" : "Alvin",
    "school" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "class" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "course" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89"
  }
}
```

Teacher表
```json
{
  "mosson":{
    "id" : "0003",
    "username" : "mosson",
    "school" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "class" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "course" : ["2ae741a3e8ed090faec3cf75e7d834481c0fca89"]
  }
}
```

School表
```json
{
  "2ae741a3e8ed090faec3cf75e7d834481c0fca89" : {
    "id" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "name" : "北京校区"
  }
}
```
stuclass表
```json
{
  "Python":{
    "name" : "Python",
    "School" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "Teacher" : ""
  }
}
```

session表
```json
{
  "sessionId" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89"
  "username" : "root"
}
```

cookie表
```json
{
    "cookie" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "session" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89"
}
```

Course 表
```json
{
  "Linux" : {
    "DateofSchool" : "2017-05-06",
    "cycle" : "5",
    "price" : 8999.00,
    "school" : "2ae741a3e8ed090faec3cf75e7d834481c0fca89",
    "stuclass" : ""
  }
}
```
