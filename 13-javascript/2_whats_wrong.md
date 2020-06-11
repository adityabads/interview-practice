# What's wrong?

## Question

The expected behavior is to click on one of three boxes to see what you've won. What's wrong?

```html
<button id="btn-0">Button 1</button>
<button id="btn-1">Button 2</button>
<button id="btn-2">Button 3</button>

<script type="text/javascript">
  const prizes = ["A Unicorn!", "A Hug!", "Fresh Laundry!"];
  for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
    document.getElementById(`btn-${btnNum}`).onclick = () => {
      alert(prizes[btnNum]);
    };
  }
</script>
```

## Answer

By the time a button is pressed, the anonymous function/closure will access `btnNum`, which is 3 after the for loop finished. Thus, we will always return `undefined`. This could be fixed by wrapping the function and passing in `btnNum` as an argument.

```html
<button id="btn-0">Button 1!</button>
<button id="btn-1">Button 2!</button>
<button id="btn-2">Button 3!</button>

<script type="text/javascript">
  const prizes = ["A Unicorn!", "A Hug!", "Fresh Laundry!"];
  for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
    document.getElementById(`btn-${btnNum}`).onclick = ((frozenBtnNum) => {
      return () => {
        alert(prizes[frozenBtnNum]);
      };
    })(btnNum);
  }
</script>
```
