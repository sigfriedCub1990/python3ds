#!/usr/bin/node

function merge_sort(a_list) {
  const mid = Math.ceil(a_list.length / 2);
  if (a_list.length > 1) {
    console.log(`Splitting: ${a_list}`);
    const left_half = a_list.slice(0, mid);
    const right_half = a_list.slice(mid);

    merge_sort(left_half);
    merge_sort(right_half);

    let i = 0;
    let j = 0;
    let k = 0;

    while (i < left_half.length && j < right_half.length) {
      if (left_half[i] <= right_half[j]) {
        a_list[k] = left_half[i];
        i++;
      } else {
        a_list[k] = right_half[j];
        j++;
      }
      k++;
    }

    while (i < left_half.length) {
      a_list[k] = left_half[i];
      i++;
      k++;
    }

    while (j < right_half.length) {
      a_list[k] = right_half[j];
      j++;
      k++;
    }
  }
  console.log(`Merging: ${a_list}`);
}

function main() {
  const a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20];
  // const a_list = [3, 2, 1];
  merge_sort(a_list);
  console.log(a_list);
}

main();
