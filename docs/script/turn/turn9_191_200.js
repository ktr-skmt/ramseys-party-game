import {dot9_191_200} from './dot9_191_200.js';for (let i = 190; i < 200; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_191_200.description[i].join('')); }