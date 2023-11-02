import { dot0 } from '../turn/dot0.js'
import { dot1 } from '../turn/dot1.js'
import { dot2 } from '../turn/dot2.js'
import { dot3 } from '../turn/dot3.js'
import { dot4 } from '../turn/dot4.js'
import { dot5 } from '../turn/dot5.js'

const turn0 = []
const turn1 = []
const turn2 = []
const turn3 = []
const turn4 = []
const turn5 = []

dot0.description.forEach(element => turn0.push(element))
dot1.description.forEach(element => turn1.push(element))
dot2.description.forEach(element => turn2.push(element))
dot3.description.forEach(element => turn3.push(element))
dot4.description.forEach(element => turn4.push(element))
dot5.description.forEach(element => turn5.push(element))

const dotGraph = [
  turn0,
  turn1,
  turn2,
  turn3,
  turn4,
  turn5,
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