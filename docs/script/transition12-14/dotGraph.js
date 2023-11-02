import { dot12 } from '../turn/dot12.js'
import { dot13 } from '../turn/dot13.js'
import { dot14 } from '../turn/dot14.js'

const turn12 = []
const turn13 = []
const turn14 = []

dot12.description.forEach(element => turn12.push(element))
dot13.description.forEach(element => turn13.push(element))
dot14.description.forEach(element => turn14.push(element))

const dotGraph = [
  turn12,
  turn13,
  turn14
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