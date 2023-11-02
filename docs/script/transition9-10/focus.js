import { showModal } from './dotGraph.js';

export const focus = () => {
  const regexEdge = /"([0-9]+-[0-9]+)"\s->\s"([0-9]+-[0-9]+)+"/;
  const regexNode = /^("[0-9]+-[0-9]+";)+$/;
  const regexNodeName = /"([0-9]+-[0-9]+)";/g;
  const edges = [];
  const nodes = [];
  const emphasized = "emphasized"
  const neighbour = "neighbour"
  dot.description.forEach(element => {
    element.map(line => regexEdge.exec(line.trim()))
      .filter(matcher => matcher != null)
      .forEach(matcher => edges.push(matcher))
    element.map(line => regexNode.exec(line.trim()))
      .filter(matcher => matcher != null)
      .forEach(matcher => {
        let m = null
        while ((m = regexNodeName.exec(matcher[0])) != null)
          nodes.push(m[1])
      })
  })
  const nodeElement = (node) => document.getElementById("node" + (nodes.indexOf(node) + 1))
  const findNode = (node, i, j) =>
    edges.filter(matcher => matcher[i] == node)
      .map(matcher => nodeElement(matcher[j]))
  const coloring = (node) => {
    findNode(node, 1, 2).concat(findNode(node, 2, 1))
      .forEach(n => n.classList.add(neighbour))
    const n = nodeElement(node)
    const turnI = n.getElementsByTagName('title')[0].innerHTML.trim().split("-");
    n.addEventListener("click", () => showModal(turnI[0], turnI[1]), false)
    n.classList.add(emphasized)
    edges.filter(matcher => matcher[1] == node || matcher[2] == node)
      .map(t => edges.indexOf(t))
      .map(index => index + 1)
      .map(i => "edge" + i)
      .map(id => document.getElementById(id))
      .forEach(edge => edge.classList.add(emphasized))
  }
  const refresh = () => {
    const remove = (className) =>
      Array.from(document.getElementsByClassName(className))
        .forEach(element => element.classList.remove(className))
    remove(emphasized)
    remove(neighbour)
  }
  nodes.forEach(node =>
    nodeElement(node).addEventListener("mouseover", () => {
      refresh()
      coloring(node)
    }, false)
  )
}