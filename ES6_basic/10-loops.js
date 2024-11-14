export default function appendToEachArrayValue(array, appendString) {
  const list = [];
  for (const value of array) {
    list.push(appendString + value);
  }
  return list;
}
