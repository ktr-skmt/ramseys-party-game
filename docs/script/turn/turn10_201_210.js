import {dot10_201_210} from './dot10_201_210.js';for (let i = 200; i < 210; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot10_201_210.description[i].join('')); }