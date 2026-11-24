import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

from lab.draw_histogram import draw


class Figure(unittest.TestCase):
    def test_data_geometry_and_nonempty_accessible_labels(self):
        path=Path(__file__).resolve().parents[1]/"figures"/"delay-histogram.svg"
        self.assertEqual(path.read_text(),draw()+"\n")
        svg=ET.parse(path).getroot()
        ns={"s":"http://www.w3.org/2000/svg"}
        self.assertEqual(svg.attrib["role"],"img")
        self.assertTrue(svg.find("s:title",ns).text)
        self.assertIn("5, 4, 0, 0, 0, 0, 1",svg.find("s:desc",ns).text)
        rects={node.attrib["id"]:node.attrib for node in svg.findall("s:rect",ns) if "id" in node.attrib}
        self.assertEqual(set(rects),{"bar-0","bar-1","bar-6"})
        self.assertEqual([(int(rects[k]["x"]),int(rects[k]["height"])) for k in sorted(rects)],
                         [(92,155),(174,124),(584,31)])
        for r in rects.values():
            self.assertEqual(int(r["y"])+int(r["height"]),266)
            self.assertEqual(int(r["width"]),82)


if __name__=="__main__":
    unittest.main()
