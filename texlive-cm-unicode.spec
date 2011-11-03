# revision 19445
# category Package
# catalog-ctan /fonts/cm-unicode
# catalog-date 2010-07-13 15:28:23 +0200
# catalog-license ofl
# catalog-version 0.7.0
Name:		texlive-cm-unicode
Version:	0.7.0
Release:	1
Summary:	Computer Modern Unicode font family
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cm-unicode
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-unicode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-unicode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Computer Modern Unicode fonts were converted from metafont
sources using mftrace with autotrace backend and fontforge.
Some characters in several fonts are copied from Blue Sky type
1 fonts released by AMS. Currently the fonts contain glyphs
from Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek
(cbgreek when available) code sets and IPA extensions (from
tipa). This font set contains 33 fonts. This archive contains
AFM, PFB and OTF versions; the OTF version of the Computer
Modern Unicode fonts works with TeX engines that directly
support OpenType features, such as XeTeX and LuaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbbx.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbi.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbl.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbmo.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbmr.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbso.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbsr.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbtl.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbto.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbx.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunbxo.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunci.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunit.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunobi.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunobx.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunorm.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunoti.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunrb.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunrm.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunsi.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunsl.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunso.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunss.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunssdc.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunst.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunsx.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmuntb.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunti.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmuntt.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmuntx.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunui.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunvi.afm
%{_texmfdistdir}/fonts/afm/public/cm-unicode/cmunvt.afm
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-ecsc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-g.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-gsc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-la.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-lasc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-lb.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-lc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-ld.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-rx.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-tc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-tipa.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-tipx.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-ux.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-uxsc.enc
%{_texmfdistdir}/fonts/enc/dvips/cm-unicode/cmu-vn.enc
%{_texmfdistdir}/fonts/map/dvips/cm-unicode/cmu.map
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbbx.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbi.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbl.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbmo.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbmr.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbso.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbsr.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbtl.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbto.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbx.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunbxo.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunci.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunit.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunobi.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunobx.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunorm.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunoti.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunrb.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunrm.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunsi.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunsl.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunso.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunss.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunssdc.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunst.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunsx.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmuntb.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunti.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmuntt.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmuntx.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunui.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunvi.otf
%{_texmfdistdir}/fonts/opentype/public/cm-unicode/cmunvt.otf
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbbx.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbi.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbl.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbmo.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbmr.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbso.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbsr.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbtl.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbto.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbx.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunbxo.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunci.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunit.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunobi.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunobx.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunorm.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunoti.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunrb.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunrm.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunsi.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunsl.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunso.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunss.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunssdc.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunst.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunsx.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmuntb.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunti.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmuntt.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmuntx.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunui.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunvi.pfb
%{_texmfdistdir}/fonts/type1/public/cm-unicode/cmunvt.pfb
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/Changes
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/FAQ
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/FontLog.txt
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/Fontmap.CMU.alias
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/Fontmap.CMU.otf
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/Fontmap.CMU.pfb
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/INSTALL
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/README
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/README.doc
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/TODO
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/cmunrm.pdf
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/cmunti.pdf
%doc %{_texmfdistdir}/doc/fonts/cm-unicode/config.cmu
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
