import { dot5 } from '../turn/dot5.js'
import { dot6 } from '../turn/dot6.js'

const turn5 = []
const turn6 = []

dot5.description.forEach(element => turn5.push(element))
dot6.description.forEach(element => turn6.push(element))

const dotGraph = [
  turn5,
  turn6,
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