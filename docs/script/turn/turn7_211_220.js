import {dot7_211_220} from './dot7_211_220.js';for (let i = 210; i < 220; i++) { d3.select(`#graph${i}`).graphviz().fade(false).renderDot(dot7_211_220.description[i].join('')); }