import { dot11 } from '../turn/dot11.js'
import { dot12 } from '../turn/dot12.js'

const turn11 = []
const turn12 = []

dot11.description.forEach(element => turn11.push(element))
dot12.description.forEach(element => turn12.push(element))

const dotGraph = [
  turn11,
  turn12,
]

const transform = () => {
  const svg = document.getElementById("graph").getElementsByTagName("svg")[0]
  const g = svg.childNodes[1]
  const tfm = svg.createSVGTransform()
  tfm.setTranslate(25.4, 214)
  g.transform.baseVal.removeItem(2)
  g.transform.baseVal.appendItem(tfm)
  g.id = "sub" + g.id
  Array.from(g.getElementsByTagName("g"))
    .forEach(element => element.id = "sub" + element.id)
}

export const showModal = (turn, i) => {
  document.getElementById("graph").innerHTML = "";
  d3.graphviz("#graph").zoom(false).fade(false).renderDot(dotGraph[turn][i - 1].join(''), transform)
  MicroModal.show('modal-graph')
}