%global tl_name cm-unicode
%global tl_revision 58661

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7.0
Release:	%{tl_revision}.1
Summary:	Computer Modern Unicode font family
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cm-unicode
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-unicode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cm-unicode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Computer Modern Unicode fonts, converted from Metafont sources using
mftrace with autotrace backend and fontforge. Some characters in several
fonts are copied from Blue Sky type 1 fonts released by AMS. Currently
the fonts contain glyphs from Latin (Metafont ec, tc, vnr), Cyrillic
(lh), Greek (cbgreek when available) code sets and IPA extensions (from
tipa). This font set contains 33 fonts. This archive contains AFM, PFB
and OTF versions; the OTF version of the Computer Modern Unicode fonts
works with TeX engines that directly support OpenType features, such as
XeTeX and LuaTeX.

