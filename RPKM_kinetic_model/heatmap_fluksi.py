# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:55:28 2020

@author: Lara
"""

from plotly.graph_objects import Data, Figure

trace1 = {
  "meta": {"columnNames": {
      "x": "Dan", 
      "y": "Reakcije", 
      "z": "CC_0 - CC_3 - CC_5 - CC_7 - CC_9 - CC_12"}}, 
  "name": "<b>a) CC</b>", 
  "type": "heatmap", 
  "xgap": 1, 
  "xsrc": "LaraBezjak:14:a5948d", 
  "x": ["Day 0", "Day 3", "Day 5", "Day 7", "Day 9", "Day 12"], 
  "ygap": 1, 
  "ysrc": "LaraBezjak:14:3088c6", 
  "y": ["1", "15", "34", "35", "45", "46", "49", "50", "53", "54", "57", "58", "59", "61", "62", "63", "64", "65", "67", "69", "74", "76", "98", "99", "101", "102", "103", "104", "105", "106", "107", "111", "112", "113", "128", "130"], 
  "zmax": 5, 
  "zmin": 0, 
  "zsrc": "LaraBezjak:14:246658,f87525,66b46b,4a2b89,5c9781,f81d1f", 
  "z": [["1", "1.107553", "1.125469", "1.357624", "1.649963", "1.548950"], 
        ["1", "1.050341", "0.892441", "0.996012", "1.299713", "0.960550"], 
        ["1", "0.901897", "0.928235", "0.860322", "1.266251", "1.314310"], 
        ["1", "1.057439", "1.465866", "1.463012", "2.073607", "2.146449"], 
        ["1", "0.965490", "0.702170", "0.598368", "0.637768", "0.454266"], 
        ["1", "0.947670", "1.277135", "1.805834", "2.794658", "2.816590"], 
        ["1", "0.990091", "1.200435", "1.225261", "1.947935", "2.155078"], 
        ["1", "0.990091", "1.200435", "1.225261", "1.947935", "2.155078"], 
        ["1", "0.988509", "0.947831", "1.222140", "1.658102", "1.789190"], 
        ["1", "1.255520", "1.367049", "1.437393", "1.937548", "2.084327"], 
        ["1", "1.534653", "1.965795", "3.155350", "4.105656", "11.943951"], 
        ["1", "1.534653", "1.767002", "2.097812", "3.402915", "3.201764"], 
        ["1", "1.231994", "1.359721", "1.560797", "2.409068", "2.612006"], 
        ["1", "0.872096", "0.839424", "0.831774", "1.007970", "0.781022"], 
        ["1", "1.158131", "1.041622", "1.285377", "1.288956", "1.608291"], 
        ["1", "1.092324", "3.297692", "17.245435", "27.001802", "87.897999"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1.072955", "1.069464", "1.047711", "1.376745", "0.907358"], 
        ["1", "1.259461", "1.926877", "2.803251", "1.666476", "1.727576"], 
        ["1", "1.047349", "1.269962", "1.607562", "1.808217", "1.503457"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "0.814421", "0.558828", "0.157902", "0.249124", "0.401635"], 
        ["1", "1.028938", "1.025907", "1.324263", "1.472888", "1.210739"], 
        ["1", "1.854147", "1.327711", "3.715258", "10.104425", "34.515972"], 
        ["1", "1.274865", "2.243678", "3.178267", "3.897088", "3.877538"], 
        ["1", "0.979011", "1.149835", "1.179245", "1.606166", "1.661578"], 
        ["1", "0.881257", "0.713992", "0.224204", "0.268955", "0.325410"], 
        ["1", "0.937697", "0.705965", "0.653770", "0.774369", "0.451800"], 
        ["1", "1.127369", "1.325677", "1.276070", "1.469031", "1.477301"], 
        ["1", "0.937697", "0.705965", "0.653770", "0.774369", "0.451800"], 
        ["1", "0.941015", "0.810985", "0.807838", "1.015818", "0.647046"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "0.901897", "0.928235", "0.860322", "1.266251", "1.314310"]], 
  "zauto": False, 
  "colorbar": {
    "title": {"text": "<b>FC</b>"}, 
    "showticklabels": True
  }, 
  "transpose": False, 
  "autocolorscale": True
}
trace2 = {
  "meta": {"columnNames": {
      "x": "Dan", 
      "y": "Reakcije", 
      "z": "HD_0 - HD_3 - HD_5 - HD_7 - HD_9 - HD_12"
    }}, 
  "name": "<b>b) HD</b>", 
  "type": "heatmap", 
  "xgap": 1, 
  "xsrc": "LaraBezjak:13:1f5c95", 
  "x": ["Day 0", "Day 3", "Day 5", "Day 7", "Day 9", "Day 12"], 
  "ygap": 1, 
  "ysrc": "LaraBezjak:13:8a381f", 
  "y": ["1", "15", "34", "35", "45", "46", "49", "50", "53", "54", "57", "58", "59", "61", "62", "63", "64", "65", "67", "69", "74", "76", "98", "99", "101", "102", "103", "104", "105", "106", "107", "111", "112", "113", "128", "130"], 
  "zmax": 5, 
  "zmin": 0, 
  "zsrc": "LaraBezjak:13:248c4c,85c5e7,e9ca03,44e52a,b66e04,b15211", 
  "z": [["1", "1.190897397", "1.290422737", "1.474946677", "1.381475492", "1.55939489"], 
        ["1", "1.023787846", "1.070200676", "1.103245457", "0.887095301", "0.742912116"], 
        ["1", "0.946413259", "0.966350085", "0.839229867", "1.000589197", "1.297475672"], 
        ["1", "1.213957669", "1.471670127", "1.628727939", "2.011351265", "2.439865546"], 
        ["1", "1.156922465", "0.835746118", "0.642960438", "0.51742279", "0.544382391"], 
        ["1", "1.139607389", "1.423728668", "2.143541383", "3.066165527", "2.841055164"], 
        ["1", "1.206179927", "1.616730603", "1.183046405", "1.213210489", "1.090208001"], 
        ["1", "1.206179927", "1.616730603", "1.183046405", "1.213210489", "1.090208001"], 
        ["1", "0.987480893", "1.052264553", "1.106699589", "1.019341987", "1.433993696"], 
        ["1", "1.171308977", "1.410221664", "1.641501463", "1.874563936", "2.419642619"], 
        ["1", "2.726317666", "6.582796483", "4.798960114", "3.487287539", "4.586792362"], 
        ["1", "2.726317666", "6.582796483", "4.798960114", "3.487287539", "3.843776168"], 
        ["1", "1.354504174", "1.530856279", "1.933680295", "2.095734081", "2.435631004"], 
        ["1", "1.141313393", "1.074982147", "1.044820756", "1.029781171", "0.843773596"], 
        ["1", "1.31668059", "1.333198581", "1.663988687", "1.649653246", "1.886582396"], 
        ["1", "1.234924338", "1.451211364", "7.961740043", "21.54338014", "22.135512"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1.174479064", "1.119185796", "1.025267948", "1.0164102", "1.018856397"], 
        ["1", "1.118369529", "1.243831306", "3.375356615", "1.32785826", "1.505011206"], 
        ["1", "0.943880516", "1.183220964", "1.362781801", "1.393385037", "1.352080325"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "0.82966766", "0.700622296", "0.447756324", "0.244717076", "0.202202961"], 
        ["1", "1.008671838", "0.960506885", "1.182456447", "1.817995845", "1.846153902"], 
        ["1", "1.519766371", "1.743845447", "7.440176826", "13.30179726", "25.89580651"], 
        ["1", "1.275596933", "2.516096213", "4.932810461", "10.95903355", "18.09251564"], 
        ["1", "0.935706867", "1.139289997", "1.303612477", "1.458525081", "1.524483382"], 
        ["1", "0.89775612", "0.764594147", "0.331620117", "0.224419624", "0.22532341"], 
        ["1", "1.071910394", "0.888850081", "0.695361813", "0.545959143", "0.619894721"], 
        ["1", "1.142966045", "1.295291454", "1.270581074", "1.404470978", "1.561154669"], 
        ["1", "1.071910394", "0.888850081", "0.695361813", "0.545959143", "0.619894721"], 
        ["1", "1.092448298", "1.075694811", "1.068940086", "0.868110184", "0.72077636"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "1", "1", "1", "1", "1"], 
        ["1", "0.946413259", "0.966350085", "0.839229867", "1.000589197", "1.297475672"]], 
  "xaxis": "x2", 
  "yaxis": "y2", 
  "zauto": False, 
  "colorbar": {"title": {"text": ""}}, 
  "showscale": False, 
  "autocolorscale": True
}

data = Data([trace1, trace2])

layout = {
  "title": {"text": "<br>"}, 
  "xaxis": {
    "type": "category", 
    "dtick": 1, 
    "range": [-0.5, 5.5], 
    "tick0": 0, 
    "title": {"text": "<b>Time [day]</b>"}, 
    "domain": [0, 0.48], 
    "tickmode": "linear", 
    "autorange": True
  }, 
  "yaxis": {
    "type": "category", 
    "range": [-0.5, 38], 
    "tick0": 0, 
    "title": {"text": "<b>Reactions</b>"}, 
    "domain": [0, 1], 
    "nticks": 130, 
    "showgrid": True, 
    "tickmode": "auto", 
    "autorange": True, 
    "zerolinewidth": 2
  }, 
  "xaxis2": {
    "side": "bottom", 
    "type": "category", 
    "range": [-0.5, 5.5], 
    "title": {"text": "<b>Time [day]</b>"}, 
    "anchor": "y2", 
    "domain": [0.52, 1], 
    "autorange": True, 
  }, 
  "yaxis2": {
    "side": "left", 
    "type": "category", 
    "range": [-0.5, 38.075819672131146], 
    "title": {"text": "<br>"}, 
    "anchor": "x2", 
    "domain": [0, 1], 
    "nticks": 130, 
    "autorange": True, 
  }, 
  "autosize": True, 
  "template": {
    "data": {
      "bar": [
        {
          "type": "bar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "table": [
        {
          "type": "table", 
          "cells": {
            "fill": {"color": "#EBF0F8"}, 
            "line": {"color": "white"}
          }, 
          "header": {
            "fill": {"color": "#C8D4E3"}, 
            "line": {"color": "white"}
          }
        }
      ], 
      "carpet": [
        {
          "type": "carpet", 
          "aaxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }, 
          "baxis": {
            "gridcolor": "#C8D4E3", 
            "linecolor": "#C8D4E3", 
            "endlinecolor": "#2a3f5f", 
            "minorgridcolor": "#C8D4E3", 
            "startlinecolor": "#2a3f5f"
          }
        }
      ], 
      "mesh3d": [
        {
          "type": "mesh3d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "contour": [
        {
          "type": "contour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "heatmap": [
        {
          "type": "heatmap", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatter": [
        {
          "type": "scatter", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "surface": [
        {
          "type": "surface", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "heatmapgl": [
        {
          "type": "heatmapgl", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "histogram": [
        {
          "type": "histogram", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "parcoords": [
        {
          "line": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}, 
          "type": "parcoords"
        }
      ], 
      "scatter3d": [
        {
          "type": "scatter3d", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattergl": [
        {
          "type": "scattergl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "choropleth": [
        {
          "type": "choropleth", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattergeo": [
        {
          "type": "scattergeo", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2d": [
        {
          "type": "histogram2d", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ], 
      "scatterpolar": [
        {
          "type": "scatterpolar", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "contourcarpet": [
        {
          "type": "contourcarpet", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }
        }
      ], 
      "scattercarpet": [
        {
          "type": "scattercarpet", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scattermapbox": [
        {
          "type": "scattermapbox", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterpolargl": [
        {
          "type": "scatterpolargl", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "scatterternary": [
        {
          "type": "scatterternary", 
          "marker": {"colorbar": {
              "ticks": "", 
              "outlinewidth": 0
            }}
        }
      ], 
      "histogram2dcontour": [
        {
          "type": "histogram2dcontour", 
          "colorbar": {
            "ticks": "", 
            "outlinewidth": 0
          }, 
          "autocolorscale": True
        }
      ]
    }, 
    "layout": {
      "geo": {
        "bgcolor": "white", 
        "showland": True, 
        "lakecolor": "white", 
        "landcolor": "white", 
        "showlakes": True, 
        "subunitcolor": "#C8D4E3"
      }, 
      "font": {"color": "#2a3f5f"}, 
      "polar": {
        "bgcolor": "white", 
        "radialaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }, 
        "angularaxis": {
          "ticks": "", 
          "gridcolor": "#EBF0F8", 
          "linecolor": "#EBF0F8"
        }
      }, 
      "scene": {
        "xaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "yaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }, 
        "zaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "gridwidth": 2, 
          "linecolor": "#EBF0F8", 
          "zerolinecolor": "#EBF0F8", 
          "showbackground": True, 
          "backgroundcolor": "white"
        }
      }, 
      "title": {"x": 0.05}, 
      "xaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "yaxis": {
        "ticks": "", 
        "gridcolor": "#EBF0F8", 
        "linecolor": "#EBF0F8", 
        "automargin": True, 
        "zerolinecolor": "#EBF0F8", 
        "zerolinewidth": 2
      }, 
      "ternary": {
        "aaxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "baxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "caxis": {
          "ticks": "", 
          "gridcolor": "#DFE8F3", 
          "linecolor": "#A2B1C6"
        }, 
        "bgcolor": "white"
      }, 
      "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#19d3f3", "#e763fa", "#fecb52", "#ffa15a", "#ff6692", "#b6e880"], 
      "hovermode": "closest", 
      "colorscale": {
        "diverging": [
          [0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], 
        "sequential": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]], 
        "sequentialminus": [
          [0, "#0508b8"], [0.0893854748603352, "#1910d8"], [0.1787709497206704, "#3c19f0"], [0.2681564245810056, "#6b1cfb"], [0.3575418994413408, "#981cfd"], [0.44692737430167595, "#bf1cfd"], [0.5363128491620112, "#dd2bfd"], [0.6256983240223464, "#f246fe"], [0.7150837988826816, "#fc67fd"], [0.8044692737430168, "#fe88fc"], [0.8938547486033519, "#fea5fd"], [0.9832402234636871, "#febefe"], [1, "#fec3fe"]]
      }, 
      "plot_bgcolor": "white", 
      "paper_bgcolor": "white", 
      "shapedefaults": {
        "line": {"width": 0}, 
        "opacity": 0.4, 
        "fillcolor": "#506784"
      }, 
      "annotationdefaults": {
        "arrowhead": 0, 
        "arrowcolor": "#506784", 
        "arrowwidth": 1
      }
    }, 
    #themeRef": "PLOTLY_WHITE"
  }, 
  "colorscale": {"sequential": [
      [0, "#440154"], [0.1111111111111111, "#482878"], [0.2222222222222222, "#3e4989"], [0.3333333333333333, "#31688e"], [0.4444444444444444, "#26828e"], [0.5555555555555556, "#1f9e89"], [0.6666666666666666, "#35b779"], [0.7777777777777778, "#6ece58"], [0.8888888888888888, "#b5de2b"], [1, "#fde725"]]}, 
  "showlegend": False, 
  "annotations": [
    {
      "x": 0, 
      "y": 38, 
      "font": {"size": 16}, 
      "text": "<b>a) CC</b>", 
      "xref": "paper", 
      "yref": "y", 
      "ayref": "y", 
      "yanchor": "top", 
      "showarrow": False
    }, 
    {
      "x": 0.54, 
      "y": 37, 
      "font": {"size": 16}, 
      "text": "<b>b) HD</b>", 
      "xref": "paper", 
      "yref": "y2", 
      "ayref": "y2", 
      "xanchor": "center", 
      "showarrow": False
    }, 
    {
      "x": 4, 
      "y": 99, 
      "text": "10.1", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 99, 
      "text": "34.5", 
      "showarrow": False
    }, 
    {
      "x": 3, 
      "y": 63, 
      "text": "17.2", 
      "showarrow": False
    }, 
    {
      "x": 4, 
      "y": 63, 
      "text": "27.0", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 63, 
      "text": "87.9", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 57, 
      "text": "11.9", 
      "showarrow": False
    }, 
    {
      "x": 4, 
      "y": 101, 
      "text": "10.9", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 101, 
      "text": "18.1", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 3, 
      "y": 99, 
      "text": "7.4", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 4, 
      "y": 99, 
      "text": "13.3", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 99, 
      "text": "25.9", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 3, 
      "y": 63, 
      "text": "7.9", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 4, 
      "y": 63, 
      "text": "21.5", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 5, 
      "y": 63, 
      "text": "22.1", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 2, 
      "y": 58, 
      "text": "6.6", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }, 
    {
      "x": 2, 
      "y": 57, 
      "text": "6.6", 
      "xref": "x2", 
      "yref": "y2", 
      "axref": "x2", 
      "ayref": "y2", 
      "showarrow": False
    }
  ]
}

fig = Figure(data=data, layout=layout)

#save image
fig.write_image("heatmap.svg", width=1400, height=700)