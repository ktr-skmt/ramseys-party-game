import {dot9_171_180} from './dot9_171_180.js';for (let i = 170; i < 180; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot9_171_180.description[i].join('')); }