import { dot8 } from '../turn/dot8.js'
import { dot9 } from '../turn/dot9.js'

const turn8 = []
const turn9 = []

dot8.description.forEach(element => turn8.push(element))
dot9.description.forEach(element => turn9.push(element))

const dotGraph = [
  turn8,
  turn9,
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